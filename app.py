from flask import Flask, render_template_string
import hashlib

app = Flask(__name__)

# Dummy payroll data
payroll_data = [
    {"name": "Ishu", "role": "Engineer", "amount": 75000},
    {"name": "Priya", "role": "Designer", "amount": 68000},
    {"name": "Siri", "role": "Manager", "amount": 92000}
]

# Dummy vendor data
vendor_data = [
    {"vendor": "ABC Supplies", "service": "Stationery", "amount": 45000},
    {"vendor": "TechServ", "service": "IT Maintenance", "amount": 82000}
]

# Fraud detection: flag if amount > 90000
def is_fraudulent(entry):
    return entry["amount"] > 90000

# Simulated encryption
def encrypt_data(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Full HTML + CSS + JS in one template
template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🏢 Corporate Payment System</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f5f8fb;
      margin: 0;
      padding: 0;
    }
    header {
      background: #1f2e4d;
      color: white;
      padding: 20px;
      text-align: center;
    }
    main {
      padding: 30px;
      max-width: 1000px;
      margin: auto;
    }
    section {
      background: white;
      padding: 20px;
      margin-bottom: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #eaeaea;
    }
    th {
      background-color: #f0f2f5;
    }
    .btn {
      padding: 10px 20px;
      background: #0077cc;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      margin-top: 10px;
    }
    .btn:hover {
      background: #005fa3;
    }
    .fraud {
      color: red;
      font-weight: bold;
    }
    .ok {
      color: green;
    }
  </style>
  <script>
    function processPayroll() {
      alert("✅ Payroll processed successfully!");
    }

    function processVendors() {
      alert("✅ Vendor payments processed!");
    }
  </script>
</head>
<body>
  <header><h1>🏢 Corporate Payment System</h1></header>
  <main>
    <section>
      <h2>👨‍💼 Employee Payroll</h2>
      <table>
        <tr><th>Name</th><th>Role</th><th>Amount</th><th>Status</th></tr>
        {% for emp in employees %}
        <tr>
          <td>{{ emp.name }}</td>
          <td>{{ emp.role }}</td>
          <td>₹{{ emp.amount }}</td>
          <td>
            {% if emp.fraud %}
              <span class="fraud">⚠️ Suspicious</span>
            {% else %}
              <span class="ok">✅ OK</span>
            {% endif %}
          </td>
        </tr>
        {% endfor %}
      </table>
      <button class="btn" onclick="processPayroll()">Process Payroll</button>
    </section>

    <section>
      <h2>🏭 Vendor Payments</h2>
      <table>
        <tr><th>Vendor</th><th>Service</th><th>Amount</th><th>Status</th></tr>
        {% for ven in vendors %}
        <tr>
          <td>{{ ven.vendor }}</td>
          <td>{{ ven.service }}</td>
          <td>₹{{ ven.amount }}</td>
          <td>
            {% if ven.fraud %}
              <span class="fraud">⚠️ Suspicious</span>
            {% else %}
              <span class="ok">✅ OK</span>
            {% endif %}
          </td>
        </tr>
        {% endfor %}
      </table>
      <button class="btn" onclick="processVendors()">Pay Vendors</button>
    </section>
  </main>
</body>
</html>
'''

@app.route("/")
def dashboard():
    employees = [
        {
            **emp,
            "fraud": is_fraudulent(emp),
            "encrypted_name": encrypt_data(emp["name"])
        } for emp in payroll_data
    ]
    vendors = [
        {
            **ven,
            "fraud": is_fraudulent(ven),
            "encrypted_vendor": encrypt_data(ven["vendor"])
        } for ven in vendor_data
    ]
    return render_template_string(template, employees=employees, vendors=vendors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)


      
      
        
   
                
