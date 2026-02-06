import axios from "axios";

// ✅ Dynamically use your Vercel Environment Variable or fallback to the live link
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "https://sme-guard.onrender.com";

const API = axios.create({
  baseURL: API_BASE_URL, 
});

export default API;

export const uploadFile = (file: File, industry: string) => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("industry", industry);
  return API.post("/upload", formData, { 
    headers: { "Content-Type": "multipart/form-data" } 
  });
};

export const getHealthScore = () => API.get("/health-score");
export const getRiskAnalysis = () => API.get("/api/v1/risk-analysis");
export const getCreditScore = () => API.get("/api/v1/credit-score");
export const getDashboardSummary = () => API.get("/api/v1/dashboard-summary");
export const getLoanEligibility = () => API.get("/loan-eligibility");

export const askCFO = (question: string, language: string) => 
  API.post("/cfo/ask", { question, language });

// ✅ RECTIFIED: Points to live Render instead of local machine
export const downloadReport = () => {
  const reportUrl = `${API_BASE_URL}/investor-report`;
  window.open(reportUrl, "_blank");
};