# app/services/health_service.py

def calculate_health(financial):
    # ✅ FIX: Handle case where no data exists in the database yet
    if financial is None:
        return {
            "score": 0,
            "status": "No Data",
            "message": "Please upload a financial statement to see your health score."
        }
    
    # Existing logic with safety check
    try:
        revenue = getattr(financial, 'revenue', 0)
        expenses = getattr(financial, 'expenses', 0)
        
        if revenue > expenses:
            score = 85
            status = "Healthy"
        else:
            score = 45
            status = "At Risk"
            
        return {
            "score": score,
            "status": status,
            "revenue": revenue,
            "expenses": expenses
        }
    except Exception as e:
        return {"score": 0, "status": "Error", "message": str(e)}