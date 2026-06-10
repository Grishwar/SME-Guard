"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const [question, setQuestion] = useState("");
  const [cfoResponse, setCfoResponse] = useState("");

  const API_URL = "https://sme-guard-finpilot.onrender.com";

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      console.log("UPLOAD RESPONSE:", data);

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }

    setLoading(false);
  };

  const askCFO = async () => {
    if (!question) return;

    try {
      const response = await fetch(`${API_URL}/ask-cfo`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question,
          language: "english",
        }),
      });

      const data = await response.json();

      setCfoResponse(data.cfo_advice || "No response");
    } catch (error) {
      console.error(error);
      alert("Failed to get CFO advice");
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 p-8 text-black">
      <div className="max-w-6xl mx-auto">

        <h1 className="text-5xl font-bold text-center mb-8">
          SME Guard AI
        </h1>

        <p className="text-center text-gray-600 mb-10">
          AI Powered SME Financial Health Platform
        </p>

        <div className="bg-white p-6 rounded-xl shadow mb-8">
          <h2 className="text-2xl font-bold mb-4">
            Upload Financial CSV
          </h2>

          <input
            type="file"
            accept=".csv"
            onChange={(e) =>
              setFile(
                e.target.files ? e.target.files[0] : null
              )
            }
          />

          <button
            onClick={handleUpload}
            className="ml-4 bg-blue-600 text-white px-6 py-2 rounded"
          >
            {loading ? "Processing..." : "Analyze"}
          </button>
        </div>

        {result && (
          <>
            <div className="grid md:grid-cols-3 gap-6 mb-8">

              <div className="bg-white p-6 rounded-xl shadow text-black">
                <h3 className="font-bold text-xl">
                  Credit Score
                </h3>

                <p className="text-4xl mt-4">
                  {result?.credit_score?.credit_score ?? "N/A"}
                </p>

                <p className="mt-2">
                  {result?.credit_score?.rating ?? "N/A"}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="font-bold text-xl">
                  Risk Level
                </h3>

                <p className="text-4xl mt-4">
                  {result?.risks?.risk_level ?? "N/A"}
                </p>
              </div>

              <div className="bg-white p-6 rounded-xl shadow">
                <h3 className="font-bold text-xl">
                  Profit
                </h3>

                <p className="text-4xl mt-4">
                  ₹ {result?.credit_score?.profit ?? "N/A"}
                </p>
              </div>

            </div>

            <div className="bg-white p-6 rounded-xl shadow mb-8">

              <h2 className="text-2xl font-bold mb-4">
                Financial Summary
              </h2>

              <p>
                Revenue: ₹ {result?.financial_data?.revenue ?? "N/A"}
              </p>

              <p>
                Debt: ₹ {result?.financial_data?.debt ?? "N/A"}
              </p>

              <p>
                Cashflow: ₹ {result?.financial_data?.cashflow ?? "N/A"}
              </p>

              <p>
                Expenses: ₹ {result?.financial_data?.expenses ?? "N/A"}
              </p>

            </div>

            <div className="bg-white p-6 rounded-xl shadow mb-8">
              <h2 className="text-2xl font-bold mb-4">
                Full API Response
              </h2>

              <pre className="overflow-auto text-sm">
                {JSON.stringify(result, null, 2)}
              </pre>
            </div>
          </>
        )}

        <div className="bg-white p-6 rounded-xl shadow">

          <h2 className="text-2xl font-bold mb-4">
            AI CFO Advisor
          </h2>

          <textarea
            className="w-full border p-3 rounded"
            rows={4}
            placeholder="Ask financial questions..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
          />

          <button
            onClick={askCFO}
            className="mt-4 bg-green-600 text-white px-6 py-2 rounded"
          >
            Ask CFO
          </button>

          {cfoResponse && (
            <div className="mt-6 p-4 bg-gray-100 rounded">
              {cfoResponse}
            </div>
          )}

        </div>

      </div>
    </main>
  );
}