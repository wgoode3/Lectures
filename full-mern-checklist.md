# Full MERN Checklist

1. Create the project folder

```
mkdir panda-dashboard
cd panda-dashboard
```

2. create the server.js and modularized folders

```
touch server.js
mkdir controllers models utils
```

3. Run npm init

```
npm init
```

(Optional) Modify package.json, set the "start" script to ```nodemon server.js```

```
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "start": "nodemon server.js"
},
```

4. Install our dependencies

```
yarn add express mongoose cors
# OR use npm
npm i express mongoose cors --save
```

5. Create the front-end ```client```

```
yarn create react-app client
# OR use create-react-app
create-react-app client
```
