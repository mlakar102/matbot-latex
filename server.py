from flask import Flask, request, send_file
import subprocess, tempfile, os

app = Flask(__name__)

@app.route("/compile", methods=["POST"])
def compile():
    latex = request.json["latex"]

    with tempfile.TemporaryDirectory() as tmpdir:
        tex = os.path.join(tmpdir, "doc.tex")

        with open(tex, "w") as f:
            f.write(latex)

        subprocess.run(["pdflatex", "doc.tex"], cwd=tmpdir)

        return send_file(os.path.join(tmpdir, "doc.pdf"),
                         mimetype="application/pdf")

app.run(host="0.0.0.0", port=10000)