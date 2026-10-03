# Frontend with JavaScript

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation and first run

Required

# Frontend with JavaScript

Complete JavaScript Fundamentals or demonstrate arrays, objects, functions and decisions first. Use the supplied three-file HTML/CSS/JS web preview or a local browser. This course teaches interactive DOM work.

Work through three weeks: nine teaching lessons, twelve exercises, two checkpoints and one independent project. Plan roughly 3–5 hours of practice per week, with time to revise. All examples are fictional. Use your own harmless practice data; keep private records and credentials out of submissions. A paid coding agent is not required.

Predict before running, change one thing, compare expected with actual output, then explain the result. Worked examples use separate data; integrate the assessed starter yourself. Save exact source and output in the corresponding exercise. An accessible project/repository link may accompany the saved source. For help, include the smallest failing code, expected result and actual error.

First task: run a greeting (or preview the three frontend starter files), change one word and run again. Submit source and output or a preview screenshot. Done when you can reopen it and reproduce the result.

## Lesson 1: structure

Required

# Lesson 1 — structure

HTML gives content a role. Find the header, main work area and two sections; each section is named by its heading. The form contains a label and input. For on the label matches id on the input, which gives the field a name and lets a label click focus it. Required expresses a constraint; maxlength limits typed text to eighty characters. Novalidate turns off browser form error bubbles so our later JavaScript can give the same helpful message for blank and all-space titles. The hint is connected with aria-describedby. The empty ul will hold li rows later. Link and script paths use the exact neighboring filenames, and defer waits until the document is parsed. Click Task name now. Break only its for value, click again and observe the failure; restore it and retest. Identify this structure in E1 and E2. Do not submit the unfinished form yet.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2rem 0; }
.card { background: white; border: 1px solid #c9d7e2; padding: 1.25rem; margin: 1rem 0; }
label { display: block; margin-top: 1rem; font-weight: 700; }
input, select, button { font: inherit; min-height: 2.75rem; }
input, select { width: 100%; }
button { background: #076b63; color: white; border: 0; padding: .5rem 1rem; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; padding: .5rem; }
.skip-link:focus { left: .5rem; }
/* TODO: create mobile-first task layout, readable task rows, and a two-column layout at 48rem. */
```

### app.js

```javascript

```


## E1: Practice after Lesson 1

Required

## E1

Mark the header, main, and two sections in the starter. Submit the matching label/input pair and explain why a placeholder alone is insufficient.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E2: Practice after Lesson 1

Required

## E2

Deliberately break the title label's `for` value, test clicking the label, then fix it. Submit before/after code and what focus did.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 2: layout

Required

# Lesson 2 — layout

CSS selects elements and sets their presentation. The star rule makes width include padding and borders. Body margin zero removes browser edge spacing. The container uses the smaller of the available width minus two rem and sixty-eight rem, then centers with auto margins. Grid display and gap stack the two sections by default. At forty-eight rem the media rule gives them two flexible columns. Minmax sets reasonable lower bounds while allowing the fractions to share extra space. Task text uses overflow-wrap so a long word cannot force the page wider. Run a narrow three-hundred-seventy-five-pixel view first, then a wide twelve-hundred-eighty-pixel view. Inspect each line and note any sideways scroll. Keep focus-visible: the orange outline identifies a keyboard target. E3 and E4 adapt this layout to your Study Plan, with your own narrow and wide screenshots.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript

```


## E3: Practice after Lesson 2

Required

## E3

Style the cards, readable text and task rows. Submit CSS and a ~375px screenshot.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E4: Practice after Lesson 2

Required

## E4

Add the 48rem two-column rule and submit a ~1280px screenshot. State whether horizontal scrolling appears in either.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 3: checks

Required

# Lesson 3 — checks

Use Tab from the browser address bar. The off-screen skip link becomes visible on focus. Press Enter on it to reach main, then continue through task name, category, Add, and filter. The order follows HTML, so do not rearrange it only with visual styling. A visible outline is evidence of where you are; do not remove it. Temporarily put a li containing Practice arrays and objects and functions before the project review this weekend into the empty list and inspect wrapping at phone width. Then remove that temporary row. Do not claim the dynamic app works yet. A mouse click and a keyboard traversal test different things. E5 records your observed order and a focus fix; E6 records long text. Checkpoint 1 needs your static source, two widths and keyboard notes. If the preview traps keys, follow the verified alternate route rather than claiming accessibility from a screenshot.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript

```


## E5: Practice after Lesson 3

Required

## E5

Record your keyboard order and fix one focus-visibility issue without removing the outline.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E6: Practice after Lesson 3

Required

## E6

Enter or temporarily display a long task title, check wrapping at narrow width, and fix overflow if needed.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 1

Required

Submit source and narrow/wide screenshots with a short semantic and keyboard checklist. The task controls may be unimplemented, but HTML structure and layout must be usable.

## Lesson 4: events

Required

# Lesson 4 — events

This lesson completes addTask before you need it in E8. Query-selector finds an element by its hash-prefixed id. The submit callback receives an event; prevent-default stops the form from navigating or reloading. Normalize-title turns the supplied value into text, trims outside whitespace, then replaces each run of spaces with one. Add-task returns two fields: either the old list plus an error, or a new list containing a new task. The square-bracket spread copies existing items; it does not mutate them. Each task has an id, title, category and false done flag. In the handler, return stops after showing an error. A valid result becomes our next state, then the id counter advances. We print the list as JSON, clear the input, and return focus to it. Enter Bring notebook with the button, then Pack water with Enter. After the second task, the status says stored two. Try only spaces: no third task is stored and Enter a task name appears. E7 first logs a trimmed title; E8 connects the now-taught helper. This focused demo stores data but deliberately leaves list rendering for the next lesson.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript
// Isolated lesson: adding data and reporting success; dynamic task rendering comes next.
let tasks = [];
let nextId = 1;
function normalizeTitle(value) { return String(value).trim().replace(/\s+/g, ' '); }
function addTask(list, title, category, id) {
  const clean = normalizeTitle(title);
  if (!clean) return { list, error: 'Enter a task name.' };
  return { list: [...list, { id, title: clean, category, done: false }], error: null };
}
const form = document.querySelector('#task-form');
const titleInput = document.querySelector('#task-title');
const categoryInput = document.querySelector('#task-category');
const status = document.querySelector('#form-status');
form.addEventListener('submit', event => {
  event.preventDefault();
  const result = addTask(tasks, titleInput.value, categoryInput.value, nextId);
  if (result.error) { status.textContent = result.error; titleInput.focus(); return; }
  tasks = result.list;
  nextId += 1;
  status.textContent = `Added ${tasks[tasks.length - 1].title}; stored ${tasks.length}`;
  console.log(JSON.stringify(tasks));
  titleInput.value = '';
  titleInput.focus();
});
```


## E7: Practice after Lesson 4

Required

## E7

Add a submit handler that prevents reload and prints the trimmed title to the console. Submit code and result for “Practice arrays.”

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E8: Practice after Lesson 4

Required

## E8

Call `addTask` from the handler, reject an all-space title, and show a helpful status message. Submit valid and invalid cases.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 5: render

Required

# Lesson 5 — render

The two seeded errands let us test rendering separately from adding. Render clears old children and builds one li per record. Create-element creates a real node; type checkbox gives the input its behavior; checked comes from state. The label points to a stable task id. Text-content displays the title as text, including angle brackets, so the second title never becomes bold markup. Append puts nodes into their parent. On change, checkbox.checked becomes the record done value; then we rebuild the view and recompute remaining work with a loop. The count chooses task at one and tasks otherwise; the ternary uses the equality test we already learned. Rebuilding removes the focused checkbox. That is why we pass its task id and focus its replacement afterward. Check the first task using Space with keyboard focus, then uncheck it without restarting Tab. Count moves two to one to two. The form in this demo intentionally does not add records. E9 and E10 now combine this taught rendering with your add handler; final integration remains your work.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript
// Isolated lesson: seeded records, safe rendering, completion and focus.
let tasks = [
  { id: 1, title: 'Bring notebook', category: 'Practice', done: false },
  { id: 2, title: '<b>Pack water</b>', category: 'Review', done: false }
];
const list = document.querySelector('#task-list');
const count = document.querySelector('#task-count');
const filter = document.querySelector('#task-filter');
const empty = document.querySelector('#empty-state');
function render(focusId = null) {
  list.replaceChildren();
  for (const task of tasks) {
    const row = document.createElement('li'); row.className = 'task';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox'; checkbox.checked = task.done; checkbox.id = `task-${task.id}`;
    const label = document.createElement('label'); label.htmlFor = checkbox.id;
    label.textContent = task.title; label.style.margin = '0';
    checkbox.addEventListener('change', () => { task.done = checkbox.checked; render(task.id); });
    row.append(checkbox, label); list.append(row);
  }
  let remaining = 0;
  for (const task of tasks) if (!task.done) remaining += 1;
  count.textContent = `${remaining} ${remaining === 1 ? 'task' : 'tasks'} remaining`;
  empty.hidden = tasks.length > 0;
  if (focusId !== null) (document.getElementById(`task-${focusId}`) || filter).focus();
}
document.querySelector('#task-form').addEventListener('submit', event => event.preventDefault());
render();
```


## E9: Practice after Lesson 5

Required

## E9

Render two tasks with text labels and test a title containing `<b>Review</b>`; it should appear as text.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E10: Practice after Lesson 5

Required

## E10

Add a checkbox that toggles completion and updates the remaining count. Submit state before/after and screenshot.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 6: filters

Required

# Lesson 6 — filters

Filter is a view setting, not deletion. Array filter visits records and keeps those whose callback returns true. The all condition keeps every record. Otherwise the ternary asks whether Done was selected: keep done tasks in that case, unfinished ones otherwise. The arrow writes the callback function; you can use an ordinary function with the same return value. Count still reads the entire array, so filtering never changes remaining work. Change reruns render when the select changes. No tasks yet describes empty data; no tasks match describes an empty view of existing data. With both tasks open, choose Done to see the no-match message. Return to All and complete the first; All shows two, To do one, Done one. In To do, keyboard-complete its remaining task: that row disappears, so focus goes to Show instead of nowhere. Do E11, E12 and Checkpoint 2 using both your valid-add and blank-input tests. Your full source must preserve data when a filter hides it.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript
// Isolated lesson: seeded records, safe rendering, completion and focus.
let tasks = [
  { id: 1, title: 'Bring notebook', category: 'Practice', done: false },
  { id: 2, title: '<b>Pack water</b>', category: 'Review', done: false }
];
const list = document.querySelector('#task-list');
const count = document.querySelector('#task-count');
const filter = document.querySelector('#task-filter');
const empty = document.querySelector('#empty-state');
function render(focusId = null) {
  const shown = tasks.filter(task => filter.value === 'all' || (filter.value === 'done' ? task.done : !task.done));
  list.replaceChildren();
  for (const task of shown) {
    const row = document.createElement('li'); row.className = 'task';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox'; checkbox.checked = task.done; checkbox.id = `task-${task.id}`;
    const label = document.createElement('label'); label.htmlFor = checkbox.id;
    label.textContent = task.title; label.style.margin = '0';
    checkbox.addEventListener('change', () => { task.done = checkbox.checked; render(task.id); });
    row.append(checkbox, label); list.append(row);
  }
  let remaining = 0;
  for (const task of tasks) if (!task.done) remaining += 1;
  count.textContent = `${remaining} ${remaining === 1 ? 'task' : 'tasks'} remaining`;
  empty.textContent = tasks.length === 0 ? 'No tasks yet. Add one to begin.' : 'No tasks match this filter.';
  empty.hidden = shown.length > 0;
  if (focusId !== null) (document.getElementById(`task-${focusId}`) || filter).focus();
}
document.querySelector('#task-form').addEventListener('submit', event => event.preventDefault());
filter.addEventListener('change', () => render());
render();
```


## E11: Practice after Lesson 6

Required

## E11

Implement all three filters, test with one open and one done task, and submit each visible set.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E12: Practice after Lesson 6

Required

## E12

Test whitespace-only input and a no-match filter; submit the two messages and code that produces them.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 2

Required

Submit source and a short test log: add two, complete one, show all/open/done, reject blank, keyboard-submit with Enter.

## Lesson 7: plan

Required

# Lesson 7 — plan

Before final integration, write a seven-row state table: no tasks, two tasks, one completed, To do, Done, blank input and a long title. Name the element that communicates each result: form status, remaining count, list or empty message. Include narrow and wide checks, a title containing angle brackets, and a checkbox that disappears under the active filter. We already taught each small mechanism; the final Study Plan combines them. The earlier Errand Practice demonstrations intentionally separate add from rendering, so they are not a finished project to copy. Decide your state owner and how the handler passes an updated array to render. If you keep const for the array, update its contents deliberately; if you use let, assign the returned new list. Do not combine two independently declared task arrays. Submit your plan before integration.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript

```


## Lesson 8: integration

Required

# Lesson 8 — integration

This partial page returns a new list from addTask and counts unfinished tasks with an ordinary loop. Trace a valid submit: the listener prevents navigation, calls the helper, checks error, updates one state owner, advances the next id, gives feedback, and clears input. Now connect the separate rendering pattern and filter pattern from earlier lessons. That connection is your final integration work. Use the ids from stored tasks, not their array positions, because filtering changes positions. Call render only after state changes. Preserve checkbox focus, or move to Show if that checkbox disappears. Show blank-name feedback near the form and return focus to the field. Keep title rendering as text. This demonstrated page still does not display dynamic task rows. Complete your own Study Plan starter and test every row of the plan. No reference answer is released before your independent submission.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript
// Isolated lesson: adding data and reporting success; dynamic task rendering comes next.
let tasks = [];
let nextId = 1;
function normalizeTitle(value) { return String(value).trim().replace(/\s+/g, ' '); }
function addTask(list, title, category, id) {
  const clean = normalizeTitle(title);
  if (!clean) return { list, error: 'Enter a task name.' };
  return { list: [...list, { id, title: clean, category, done: false }], error: null };
}
const form = document.querySelector('#task-form');
const titleInput = document.querySelector('#task-title');
const categoryInput = document.querySelector('#task-category');
const status = document.querySelector('#form-status');
form.addEventListener('submit', event => {
  event.preventDefault();
  const result = addTask(tasks, titleInput.value, categoryInput.value, nextId);
  if (result.error) { status.textContent = result.error; titleInput.focus(); return; }
  tasks = result.list;
  nextId += 1;
  status.textContent = `Added ${tasks[tasks.length - 1].title}; stored ${tasks.length}`;
  console.log(JSON.stringify(tasks));
  titleInput.value = '';
  titleInput.focus();
});

// Transfer demonstration: the returned list is the next state. Integration is learner work.
function remainingCount(list) {
  let total = 0;
  for (const task of list) if (!task.done) total += 1;
  return total;
}
console.log('Empty remaining: ' + remainingCount([]));
```


## Independent final project

Required

 — finish and explain

### Lesson 7 — plan the Study Plan project

Sketch the states before editing code: zero tasks; two tasks; one completed; open filter; done filter; blank title; long title. Mark which element communicates each state. Plan mobile first, then wide. **Submit:** a seven-row state/expected-screen table, two CSS breakpoints or a reason for one, and a keyboard path. **Done when:** another learner could test your plan.

### Lesson 8 — integrate and test

Complete `starter/app.js` and the CSS TODO. Required features: validated add; completion toggle; all/open/done filter; remaining count; correct empty messages; responsive layout; keyboard access; visible focus; safe text rendering. **Test:** blank title, two tasks, keyboard-toggle once and back, focus remaining on its checkbox; keyboard-toggle under To do so a disappearing row moves focus to Show; each filter, long title, ~375px and ~1280px, Tab and Enter. Submit exact source and observed results. The project intentionally resets on reload. **Done when:** all cases match your plan.

### Lesson 9 — share and revise

Paste your final source and test log in Learn or provide a stable repository link if offered in your actual exercise. Add narrow/wide screenshots and one problem you found, the change you made, and a retest. Explain why your title rendering uses `textContent`. Compare your work with the 10-point rubric in the project rubric below.  **Done when:** a reviewer can reproduce your page from the exact submitted files.



## Independent work

Use the unfinished starter. Explain your integration and one failed-then-repaired case. The assessed reference is released only after submission.

## Rubric (10 points)

Add/complete/filter/count4;responsive structure,labels,keyboard,visible focus3;validation,safe text,readability2;explanation and revision1.
### app.js

```javascript
// Tasks intentionally reset when the page reloads. No account or storage is required.
const tasks = [];
let nextId = 1;

function normalizeTitle(value) {
  // TODO: trim outside spaces and collapse repeated inside spaces.
}
function addTask(list, title, category, id) {
  // TODO: reject blank names; return a new list with { id, title, category, done: false }.
}
function toggleTask(list, id) {
  // TODO: return a new list with only the matching task's done value changed.
}
function visibleTasks(list, filter) {
  // TODO: all, open, or done.
}
function remainingCount(list) {
  // TODO: count tasks not done.
}

const form = document.querySelector('#task-form');
const titleInput = document.querySelector('#task-title');
const categoryInput = document.querySelector('#task-category');
const filterInput = document.querySelector('#task-filter');
const listElement = document.querySelector('#task-list');
const countElement = document.querySelector('#task-count');
const emptyElement = document.querySelector('#empty-state');
const statusElement = document.querySelector('#form-status');

function render() {
  // TODO: clear list; create one li, checkbox, and text label per visible task.
  // Use textContent for student-entered text. Update count and empty message.
}
form.addEventListener('submit', event => {
  event.preventDefault();
  // TODO: add a valid task, show a status message, reset/focus input, and render.
});
filterInput.addEventListener('change', render);
render();
```

### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Study Plan</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to study plan</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Study Plan</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Practice arrays”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2rem 0; }
.card { background: white; border: 1px solid #c9d7e2; padding: 1.25rem; margin: 1rem 0; }
label { display: block; margin-top: 1rem; font-weight: 700; }
input, select, button { font: inherit; min-height: 2.75rem; }
input, select { width: 100%; }
button { background: #076b63; color: white; border: 0; padding: .5rem 1rem; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; padding: .5rem; }
.skip-link:focus { left: .5rem; }
/* TODO: create mobile-first task layout, readable task rows, and a two-column layout at 48rem. */
```


### Independent project review

Use the published point weights. Individual scoring applies only when included in the learner’s enrollment. Self-paced learners can use these criteria for self-review.

- **Functional tracker (4 points):** Add tasks, complete tasks, filter all/open/done and display the correct counts.
- **Responsive and accessible interface (3 points):** Use responsive structure, semantic labels, keyboard operation and visible focus.
- **Validation and safe rendering (2 points):** Reject invalid input, render titles as text and keep code readable.
- **Explanation and revision (1 point):** Explain state/event/render flow and make one focused improvement. Guided pass requires 8/10 with add and complete working.

## Lesson 9: review

Required

# Lesson 9 — review

Review is a sequence, not a statement that it works. On your own integrated page add two fictional tasks, complete one and undo it, then try all filters. Reject an all-space title. Type a long title and an angle-bracket title. Check the page at both widths. Use only keyboard for Add, Show and completion; a removed filtered row must send focus to Show. On this separate practice page we can inspect safe title handling: temporarily replace label.textContent with label.innerHTML and see Pack water become markup. Restore textContent immediately; the literal characters return. This is a demonstration of why user text is not trusted HTML, not a reason to add sanitization machinery to this tiny exercise. Submit all three source files, screenshots, exact keyboard notes and one bug with its retest. Tasks reset on reload in the required project. Persistence is optional after submission. Personal scoring depends on your enrollment; an agent subscription is unnecessary.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.
### index.html

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Errand Practice</title>
  <link rel="stylesheet" href="styles.css">
  <script src="app.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to errand practice</a>
  <header class="site-header"><div class="container"><p class="eyebrow">CSG practice project</p><h1>Errand Practice</h1><p>Keep your next learning steps in one place.</p></div></header>
  <main id="main" class="container grid">
    <section class="card" aria-labelledby="add-heading">
      <h2 id="add-heading">Add a task</h2>
      <form id="task-form" novalidate>
        <label for="task-title">Task name</label>
        <input id="task-title" name="title" maxlength="80" required aria-describedby="title-hint">
        <p id="title-hint" class="hint">Use a short action, such as “Bring notebook”.</p>
        <label for="task-category">Category</label>
        <select id="task-category" name="category"><option>Practice</option><option>Project</option><option>Review</option></select>
        <button type="submit">Add task</button>
      </form>
      <p id="form-status" role="status" aria-live="polite"></p>
    </section>
    <section class="card" aria-labelledby="tasks-heading">
      <div class="section-heading"><h2 id="tasks-heading">Your tasks</h2><p id="task-count" aria-live="polite">0 tasks remaining</p></div>
      <label for="task-filter">Show</label>
      <select id="task-filter"><option value="all">All tasks</option><option value="open">To do</option><option value="done">Done</option></select>
      <p id="empty-state">No tasks yet. Add one to begin.</p>
      <ul id="task-list" aria-label="Study tasks"></ul>
    </section>
  </main>
  <footer class="container"><p>Practice project. Tasks reset when this page reloads.</p></footer>
</body>
</html>
```

### styles.css

```css
:root { color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; color: #16283d; background: #f4f7fa; }
* { box-sizing: border-box; }
body { margin: 0; }
.container { width: min(100% - 2rem, 68rem); margin-inline: auto; }
.site-header { background: #123653; color: white; padding: 2.5rem 0; }
.site-header h1 { font-size: clamp(2rem, 6vw, 3.75rem); margin: .1rem 0; line-height: 1.1; }
.eyebrow { color: #b8e8df; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
.grid { display: grid; gap: 1.25rem; padding-block: 1.5rem; }
.card { background: white; border: 1px solid #c9d7e2; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 8px 24px #12365312; }
h2 { margin-top: 0; }
label { display: block; font-weight: 700; margin: 1rem 0 .25rem; }
input, select, button { font: inherit; border-radius: .45rem; padding: .65rem .75rem; min-height: 2.75rem; }
input, select { width: 100%; border: 1px solid #698296; background: white; color: inherit; }
button { border: 0; background: #076b63; color: white; font-weight: 700; cursor: pointer; }
button:hover { background: #07554f; }
:focus-visible { outline: 3px solid #cf6d12; outline-offset: 3px; }
.hint { font-size: .9rem; color: #40566b; margin: .25rem 0; }
.section-heading { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: .5rem; }
#task-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.task { display: flex; gap: .75rem; align-items: flex-start; padding: .8rem 0; border-top: 1px solid #d7e1e8; }
.task input { width: auto; flex: none; margin-top: .3rem; }
.task strong { display: block; overflow-wrap: anywhere; }
.task small { color: #40566b; }
.task.done strong { text-decoration: line-through; }
.skip-link { position: absolute; left: -10000px; top: .5rem; background: white; color: #123653; padding: .5rem; }
.skip-link:focus { left: .5rem; z-index: 2; }
footer { color: #40566b; padding-bottom: 2rem; }
@media (min-width: 48rem) { .grid { grid-template-columns: minmax(16rem, 2fr) minmax(20rem, 3fr); align-items: start; gap: 2rem; } .card { padding: 1.75rem; } }
```

### app.js

```javascript
// Isolated lesson: seeded records, safe rendering, completion and focus.
let tasks = [
  { id: 1, title: 'Bring notebook', category: 'Practice', done: false },
  { id: 2, title: '<b>Pack water</b>', category: 'Review', done: false }
];
const list = document.querySelector('#task-list');
const count = document.querySelector('#task-count');
const filter = document.querySelector('#task-filter');
const empty = document.querySelector('#empty-state');
function render(focusId = null) {
  const shown = tasks.filter(task => filter.value === 'all' || (filter.value === 'done' ? task.done : !task.done));
  list.replaceChildren();
  for (const task of shown) {
    const row = document.createElement('li'); row.className = 'task';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox'; checkbox.checked = task.done; checkbox.id = `task-${task.id}`;
    const label = document.createElement('label'); label.htmlFor = checkbox.id;
    label.textContent = task.title; label.style.margin = '0';
    checkbox.addEventListener('change', () => { task.done = checkbox.checked; render(task.id); });
    row.append(checkbox, label); list.append(row);
  }
  let remaining = 0;
  for (const task of tasks) if (!task.done) remaining += 1;
  count.textContent = `${remaining} ${remaining === 1 ? 'task' : 'tasks'} remaining`;
  empty.textContent = tasks.length === 0 ? 'No tasks yet. Add one to begin.' : 'No tasks match this filter.';
  empty.hidden = shown.length > 0;
  if (focusId !== null) (document.getElementById(`task-${focusId}`) || filter).focus();
}
document.querySelector('#task-form').addEventListener('submit', event => event.preventDefault());
filter.addEventListener('change', () => render());
render();
```


## Optional review after independent submission

Optional



The required project and rubric above are completed and explained without an agent. After that submission, offer the optional agent-assisted extension. The learner can use Codex desktop, another coding agent they already have, or the saved code and tests without an AI account. They inspect the proposed change and rerun the original project before accepting it. No AI subscription or optional-extension score is required to pass.

**Expected checks:** Original add/toggle/filter still work; fictional tasks survive reload where browser storage is available; invalid/blocked storage falls back safely. Write tests in your own project for the original behavior and the changed-data/edge cases listed above. Staff assessment tests are not a learner dependency. Ask for a prompt or change request, one accepted or rejected line with a reason, the original and extended outputs, and one edge-case test.  Follow the optional recorded example in this lesson after submitting your independent project.


This is optional and does not affect required completion. You may use an agent you already have or review the saved change without an account. Request instructor release of the review fixture after the independent project.
