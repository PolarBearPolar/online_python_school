let editor;

function initPythonEditor(editorElementId) {
    // Define Python editor element
    editor = CodeMirror.fromTextArea(
        document.getElementById(editorElementId),
        {
            mode: "python",
            theme: "darcula",
            lineNumbers: true
        }
    );
}

function executePythonCode(runCodeBtnId, editorOutputElementId, CSRFToken) {
// Do action on button click
    document.getElementById(runCodeBtnId).addEventListener("click", () => {
        // Send POST request to backend and get response
        data = JSON.stringify({
            pytonScript: editor.getValue()
        })
        let response = fetch("", {
            method: "POST",
            body: data,
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json',
                'X-CSRFToken': CSRFToken
            },
        }).then(
            response => response.json()
        ).then(
            // Output response (Python script output) to editor element
            data => document.getElementById(editorOutputElementId).innerText = data.pytonScripOutput
        ).catch(
            error => console.error("Error: ", error)
        )
    });
}