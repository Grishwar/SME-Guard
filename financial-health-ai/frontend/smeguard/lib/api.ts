import axios from "axios";

const API = axios.create({
  baseURL: "https://sme-guard.onrender.com", 
});

export default API;

// Supports CSV, XLSX, and PDF as per requirements
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

// PDF Engine Implementation
export const downloadReport = () => 
  API.get("/investor-report", { responseType: 'blob' });