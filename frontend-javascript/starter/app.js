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
