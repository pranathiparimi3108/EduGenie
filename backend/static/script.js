const featureSelect = document.getElementById("feature");
const extraFields = document.getElementById("extra-fields");
const output = document.getElementById("output");
const generateBtn = document.getElementById("generate-btn");

const endpoints = {
  explain: "/api/explain",
  "learning-path": "/api/learning-path",
  quiz: "/api/quiz",
  qna: "/api/qna",
  summary: "/api/summary",
};

function renderExtraFields() {
  const feature = featureSelect.value;
  extraFields.innerHTML = "";

  if (feature === "qna") {
    extraFields.innerHTML = `
      <label for="question">Question</label>
      <textarea id="question" rows="3" placeholder="Ask your doubt here"></textarea>
      <label for="context">Context (optional)</label>
      <input id="context" type="text" placeholder="Subject or chapter" />
    `;
  }

  if (feature === "summary") {
    extraFields.innerHTML = `
      <label for="content">Content to summarize</label>
      <textarea id="content" rows="5" placeholder="Paste notes or chapter text"></textarea>
    `;
  }
}

async function generate() {
  const feature = featureSelect.value;
  const topic = document.getElementById("topic").value.trim();
  const endpoint = endpoints[feature];

  let payload = { topic };

  if (feature === "qna") {
    payload = {
      question: document.getElementById("question").value.trim(),
      context: document.getElementById("context").value.trim(),
    };
    if (!payload.question) {
      output.textContent = "Please enter a question.";
      return;
    }
  } else if (feature === "summary") {
    payload = {
      content: document.getElementById("content").value.trim(),
    };
    if (!payload.content) {
      output.textContent = "Please enter content to summarize.";
      return;
    }
  } else if (!topic) {
    output.textContent = "Please enter a topic.";
    return;
  }

  generateBtn.disabled = true;
  output.textContent = "Generating...";

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || "Request failed");
    }
    output.textContent = data.result || JSON.stringify(data, null, 2);
  } catch (error) {
    output.textContent = `Error: ${error.message}`;
  } finally {
    generateBtn.disabled = false;
  }
}

featureSelect.addEventListener("change", renderExtraFields);
generateBtn.addEventListener("click", generate);
renderExtraFields();
