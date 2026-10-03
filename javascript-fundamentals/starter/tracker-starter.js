// JavaScript Fundamentals final project. Change the sample data only after your first run.
const EXPENSES = [
  { name: "Groceries", category: "Food", amount: 42 },
  { name: "Bus", category: "Transport", amount: 18 },
  { name: "Lunch", category: "Food", amount: 13 },
  { name: "Notebook", category: "Supplies", amount: 9 },
  { name: "Fuel", category: "Transport", amount: 30 },
  { name: "Snack", category: "Food", amount: 6 },
];
const BUDGET = 120;

function totalAmount(expenses) {
  // TODO: return the sum. Empty list => 0.
}

function totalsByCategory(expenses) {
  // TODO: return an object, for example { Food: 61 }.
}

function totalForCategory(expenses, category) {
  // TODO: sum only matching categories; absent category => 0.
}

function largestExpense(expenses) {
  // TODO: return an expense object, or null for an empty list.
}

function budgetStatus(total, budget) {
  // TODO: return "Under by N", "On budget", or "Over by N".
}

function makeReport(expenses, budget) {
  // TODO: return a readable string with total, categories, largest, and status.
}

console.log(makeReport(EXPENSES, BUDGET));
