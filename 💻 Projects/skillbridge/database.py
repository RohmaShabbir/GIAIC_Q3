class JSONDatabase:
    def __init__(self, db_file="skillbridge_db.json"):
        self.db_file = db_file
        if not os.path.exists(db_file):
            with open(db_file, 'w') as f:
                json.dump({
                    "users": [],
                    "clients": [],
                    "projects": [],
                    "invoices": [],
                    "notes": []
                }, f)
    
    def load_data(self):
        with open(self.db_file, 'r') as f:
            return json.load(f)
    
    def save_data(self, data):
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_user(self, user):
        data = self.load_data()
        data["users"].append(user.to_dict())
        self.save_data(data)
    
    def get_user(self, username):
        data = self.load_data()
        for user in data["users"]:
            if user["username"] == username:
                return user
        return None
    
    def add_client(self, client):
        data = self.load_data()
        data["clients"].append(client.to_dict())
        self.save_data(data)
    
    def get_clients(self, user_id):
        data = self.load_data()
        return [client for client in data["clients"] if client["user_id"] == user_id]
    
    def add_project(self, project):
        data = self.load_data()
        data["projects"].append(project.to_dict())
        self.save_data(data)
    
    def get_projects(self, user_id):
        data = self.load_data()
        return [project for project in data["projects"] if project["user_id"] == user_id]
    
    def add_invoice(self, invoice):
        data = self.load_data()
        data["invoices"].append(invoice.to_dict())
        self.save_data(data)
    
    def get_invoices(self, project_id=None, user_id=None):
        data = self.load_data()
        invoices = data["invoices"]
        
        if project_id:
            invoices = [inv for inv in invoices if inv["project_id"] == project_id]
        
        if user_id:
            # Get all projects for user
            user_projects = self.get_projects(user_id)
            project_ids = [p["project_id"] for p in user_projects]
            invoices = [inv for inv in invoices if inv["project_id"] in project_ids]
        
        return invoices
    
    def update_invoice_status(self, invoice_id, is_paid):
        data = self.load_data()
        for invoice in data["invoices"]:
            if invoice["invoice_id"] == invoice_id:
                invoice["is_paid"] = is_paid
                break
        self.save_data(data)
    
    def add_note(self, note):
        data = self.load_data()
        data["notes"].append(note)
        self.save_data(data)
    
    def get_notes(self, user_id):
        data = self.load_data()
        return [note for note in data["notes"] if note["user_id"] == user_id]

db = JSONDatabase()