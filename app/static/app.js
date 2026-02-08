async function analyze() {

    const resume = document.getElementById("resume").value;
    const job = document.getElementById("job").value;
    const resultBox = document.getElementById("result");

    if (!resume || !job) {
        resultBox.textContent = "Please enter both resume text and job description.";
        return;
    }

    resultBox.textContent = "Analyzing...";

    try {

        const response = await fetch("/resume_analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume_text: resume,
                job_description: job
            })
        });

        if (!response.ok) {
            const err = await response.text();
            resultBox.textContent = "Error:\n" + err;
            return;
        }

        const data = await response.json();

        resultBox.textContent = JSON.stringify(data, null, 2);

    } catch (e) {
        resultBox.textContent = "Request failed:\n" + e.toString();
    }
}