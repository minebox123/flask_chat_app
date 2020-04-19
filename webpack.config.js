const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");


module.exports = {
    context: path.resolve(__dirname, "src/ui"),
    entry: "./Views/index.js",
    output: {
        path: path.resolve(__dirname, "src/public"),
        filename: "[name].bundle.js",
        publicPath: "/"
    },
    devServer: {
        historyApiFallback: true
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ["babel-loader"]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./Views/index.html"
        })
    ],
    resolve: {
        extensions: [".js", ".jsx"]
    }
}