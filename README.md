# flask-vercel

This repo is to test the deploy to Vercel

## Test local

```
virtualenv ~/.ve/vercel
source ~/.ve/vercel/bin/activate
pip install -r requirements.txt
FLASK_APP=index.py flask run

# 🚀 go to http://localhost:5000
```

## Deploy to vercel

- Create an account at https://vercel.com/
- Install the Vercel CLI: `npm i -g vercel`

Then, inside your repo folder, run `vercel`:

```
(vercel) ➜  flask-vercel$ vercel
Vercel CLI 23.0.1
? Set up and deploy “~/workspace/workon/flask-vercel”? [Y/n] y
? Which scope do you want to deploy to? your-vercel-account
? Link to existing project? [y/N] n
? What’s your project’s name? flask-vercel
? In which directory is your code located? ./
...
```

Done! You should access your very simple flask app running on Vercel
