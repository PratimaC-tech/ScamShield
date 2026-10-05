document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("analyzeForm");

  const highExample = `Congratulations! You have been selected for a remote internship.
Pay a refundable registration fee of ₹1999 today to confirm your seat.
Send your Aadhaar and bank details immediately. Offer expires today.`;

  const lowExample = `You are invited to interview for the Software Intern position.
The interview will be conducted through the company's official careers process.
No payment is requested. Please review the job description before the interview.`;

  const message = document.getElementById("offerMessage");
  const url = document.getElementById("offerUrl");

  document.getElementById("highExample")?.addEventListener("click", () => {
    message.value = highExample;
    url.value = "https://example.com/careers/internship";
  });

  document.getElementById("lowExample")?.addEventListener("click", () => {
    message.value = lowExample;
    url.value = "https://example.com/careers/software-intern";
  });

  form?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const loading = document.getElementById("loading");
    const error = document.getElementById("error");
    error.classList.add("hidden");
    loading.classList.remove("hidden");

    try {
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          message: message.value,
          url: url.value
        })
      });

      const data = await response.json();

      if (!response.ok) throw new Error(data.error || "Analysis failed.");

      sessionStorage.setItem("scamshieldReport", JSON.stringify(data));
      window.location.href = "/report";
    } catch (err) {
      error.textContent = err.message;
      error.classList.remove("hidden");
    } finally {
      loading.classList.add("hidden");
    }
  });

  const reportContent = document.getElementById("reportContent");

  if (reportContent) {
    const raw = sessionStorage.getItem("scamshieldReport");

    if (raw) {
      const data = JSON.parse(raw);
      document.getElementById("reportEmpty").classList.add("hidden");
      reportContent.classList.remove("hidden");

      document.getElementById("score").textContent = data.risk_score;
      document.getElementById("riskLevel").textContent = data.risk_level;
      document.getElementById("recommendation").textContent = data.recommendation;
      document.getElementById("disclaimer").textContent = data.disclaimer;

      const levelBox = document.getElementById("levelBox");
      levelBox.classList.add(
        data.risk_level === "HIGH" ? "level-high" :
        data.risk_level === "MEDIUM" ? "level-medium" : "level-low"
      );

      const signals = document.getElementById("signals");

      if (!data.signals.length) {
        signals.innerHTML = `<div class="report-signal"><h3>✅ No major warning pattern detected</h3><p>The current rule set did not detect a major warning signal. Continue with independent verification.</p></div>`;
      } else {
        signals.innerHTML = data.signals.map(s => `
          <article class="report-signal">
            <h3>${escapeHtml(s.title)}</h3>
            <p>${escapeHtml(s.explanation)}</p>
            ${s.matches?.length ? `<div class="matches">Detected: ${s.matches.map(escapeHtml).join(", ")}</div>` : ""}
          </article>
        `).join("");
      }
    }
  }

  const checks = document.querySelectorAll(".check-item input");
  const progressBar = document.getElementById("progressBar");
  const progressText = document.getElementById("progressText");

  function updateProgress() {
    if (!checks.length) return;
    const done = [...checks].filter(c => c.checked).length;
    progressBar.style.width = `${(done / checks.length) * 100}%`;
    progressText.textContent = `${done} of ${checks.length} checks completed`;
  }

  checks.forEach(c => c.addEventListener("change", updateProgress));
  updateProgress();
});

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, char => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
  }[char]));
}
