import os
from app import create_app

app = create_app()

'''
if __name__ == '__main__':
    app.run("0.0.0.0",5000)
'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))