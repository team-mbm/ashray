module.exports = {  
    entry: "./app/app.js",
    output: {
        path: __dirname + "/dist/js/",
        filename: "bundle.js",
        sourceMapFilename: "bundle.js.map",
    },

    watch: true,

    // eslint config
    loader: {
      configFile: './config/eslint.json'
    },

    module: {
     /*   preLoaders: [],*/
        loaders: [
           {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: "eslint-loader"
        },
          { test: /\.css$/, loader: "style!css" },
          { test: /\.html$/, loader: "mustache-loader" },
          { test: /\.json$/, loader: "json-loader" }]
    },

    resolve: {
        extensions: ['.js']
    }
};