"""Public acceptance examples. Run with your file or staff reference via env."""
import importlib
import os
import unittest
m=importlib.import_module(os.environ.get('CSG_STUDENT_MODULE','student_triage'))
GOOD={'category':'lesson','urgency':'routine','reason':'Fictional content question.'}
PROPOSED={'status':'proposed','review_required':True,'result':GOOD}

class StudentContractTest(unittest.TestCase):
    def test_input_boundaries(self):
        self.assertEqual(m.clean_message(' fictional '),'fictional')
        self.assertEqual(m.clean_message('x'*500),'x'*500)
        self.assertEqual(m.clean_message('How do I reset my password?'),'How do I reset my password?')
        for value in ('',' '*3,'x'*501,None,[], 'password is FICTIONAL_ONLY', 'api_key=FICTIONAL_ONLY'):
            with self.subTest(value=value),self.assertRaises(ValueError): m.clean_message(value)

    def test_output_boundaries(self):
        self.assertEqual(m.parse_proposal(GOOD),GOOD)
        for value in ([],{**GOOD,'category':[]},{**GOOD,'urgency':None},{**GOOD,'reason':' '},{**GOOD,'reason':'x'*121},{**GOOD,'extra':1}):
            with self.subTest(value=value),self.assertRaises(ValueError): m.parse_proposal(value)

    def test_no_call_when_input_blocked(self):
        calls=[]
        result=m.run_triage('token=FICTIONAL_ONLY',lambda text:calls.append(text))
        self.assertEqual(result['status'],'blocked');self.assertTrue(result['review_required']);self.assertEqual(calls,[])

    def test_timeout_and_bad_result_need_review(self):
        def fail(_): raise TimeoutError('FICTIONAL_PRIVATE_DIAGNOSTIC')
        for predict in (fail,lambda _:[],lambda _:{**PROPOSED,'result':{**GOOD,'category':[]}}):
            result=m.run_triage('fictional',predict)
            self.assertEqual(result['status'],'review_needed');self.assertTrue(result['review_required']);self.assertNotIn('DIAGNOSTIC',str(result))

    def test_proposal_still_requires_review_and_one_call(self):
        calls=[]
        def predict(message):calls.append(message);return PROPOSED
        result=m.run_triage(' fictional ',predict)
        self.assertEqual(result['result'],GOOD);self.assertTrue(result['review_required']);self.assertEqual(calls,['fictional'])

    def test_access_limit_does_not_retry(self):
        self.assertEqual(m.run_triage('fictional',lambda _:{'status':'access_limited','review_required':True})['status'],'access_limited')

    def test_evaluation_denominator_includes_failures(self):
        cases=[{'id':'a','message':'fictional','category':'lesson','urgency':'routine'}, {'id':'b','message':'fictional','category':'account','urgency':'urgent','ambiguous':True}]
        r=m.evaluate_cases(cases,lambda _:PROPOSED)
        self.assertEqual((r['count'],r['category_matches'],r['urgency_matches'],r['fallbacks']),(2,1,1,0));self.assertTrue(r['cases'][1]['ambiguous']);self.assertNotIn('message',str(r))
        self.assertEqual(m.evaluate_cases(cases,lambda _:{'status':'review_needed','review_required':True})['fallbacks'],2)
        with self.assertRaises(ValueError):m.evaluate_cases([],lambda _:PROPOSED)

    def test_unknown_cost_is_not_zero_cost(self):
        rows=[{'status':'proposed','metrics':{'estimated_usd':0}}, {'status':'review_needed'}, {'status':'proposed','metrics':{'estimated_usd':0.000045}}]
        self.assertEqual(m.summarize_attempts(rows),{'attempts':3,'fallbacks':1,'known_estimated_usd':0.000045,'unknown_cost_attempts':1})
        with self.assertRaises(ValueError):m.summarize_attempts([])
        malformed=[{'status':'review_needed','metrics':None}, {'status':'proposed','metrics':{'estimated_usd':float('nan')}}, {'status':'proposed','metrics':{'estimated_usd':-1}}]
        self.assertEqual(m.summarize_attempts(malformed)['unknown_cost_attempts'],3)

    def test_human_review_validates_labels(self):
        self.assertEqual(m.human_review(PROPOSED,'account','urgent'),{'status':'human_reviewed','category':'account','urgency':'urgent','changed':True})
        for label in ('other',[],None):
            with self.assertRaises(ValueError):m.human_review(PROPOSED,label,'routine')

if __name__=='__main__':unittest.main()
