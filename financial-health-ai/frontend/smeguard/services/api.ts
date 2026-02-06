import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000", 
});

export default API;

export const uploadCSV = (file: File, industry: string) => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("industry", industry);
  return API.post("/upload", formData, { headers: { "Content-Type": "multipart/form-data" } });
};

// All functions separate as per your request
export const getRiskAnalysis = () => API.get("/api/v1/risk-analysis");
export const getCreditScore = () => API.get("/api/v1/credit-score");
export const getHealthScore = () => API.get("/health-score");
export const getBankruptcyCheck = () => API.get("/bankruptcy-check");
export const getLoanEligibility = () => API.get("/loan-eligibility");
export const getDashboardSummary = () => API.get("/api/v1/dashboard-summary");

export const askCFO = (question: string, language: string) => 
  API.post("/cfo/ask", { question, language });

export const downloadReport = () => 
  API.get("/investor-report", { responseType: 'blob' });