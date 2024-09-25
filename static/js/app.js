window.onload = function() {
    fetchSessions();
};

function fetchSessions() {
    fetch("/session/sessions")
        .then(response => response.json())
        .then(data => {
            const sessionSelect = document.getElementById('sessionSelect');
            data.data.forEach(session => {
                const option = document.createElement('option');
                option.value = session.id;
                option.text = session.session_name;
                sessionSelect.add(option);
            });
        });
}

function searchKeys() {
    const session = document.getElementById("sessionSelect").value;
    const pattern = document.getElementById("searchInput").value;

    if (!session) {
        alert("Please select a Redis session.");
        return;
    }

    if (!pattern) {
        alert("Please enter a search pattern.");
        return;
    }

    fetch(`/search?pattern=${encodeURIComponent(pattern)}&session_id=${session}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "";  // 기존 결과 초기화
            if (data.keys.length > 0) {
                data.keys.forEach(key => {
                    const p = document.createElement("p");
                    p.textContent = key;
                    resultsDiv.appendChild(p);
                });
            } else {
                resultsDiv.innerHTML = "<p>No keys found.</p>";
            }
        });
}
