# Full MERN Checklist

### Create the project folder

```shell
mkdir panda-dashboard
cd panda-dashboard
```

### Create the server.js and modularized folders

```shell
touch server.js
mkdir controllers models utils
```

### Run npm init

```shell
npm init
```

#### (Optional) Modify package.json, set the "start" script to ```nodemon server.js```

```javascript
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "start": "nodemon server.js"
},
```

### Install our dependencies

```shell
yarn add express mongoose cors
# OR use npm
npm i express mongoose cors --save
```

### Create the front-end ```client```

```shell
yarn create react-app client
# OR use create-react-app
create-react-app client
```

### Install the front-end dependencies

```shell
cd client
yarn add axios react-router react-router-dom
# OR using npm
npm i axios react-router react-router-dom --save
```

### TODO - add more steps
