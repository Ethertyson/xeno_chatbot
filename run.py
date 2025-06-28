# Created by Pritanshu on 2025-05-28

from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    print("Starting Flask app...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
