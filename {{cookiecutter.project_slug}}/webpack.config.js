var webpack = require('webpack');
var path = require('path');
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var CommonsChunkPlugin = require("webpack/lib/optimize/CommonsChunkPlugin");
var BundleTracker = require('webpack-bundle-tracker');
var CleanWebpackPlugin = require('clean-webpack-plugin');

var BUILD_DIR = path.resolve(__dirname, 'static/build');
var APP_DIR = path.resolve(__dirname, 'client');

var config = {
  entry: {
    vendor: ['react', 'react-dom', 'prop-types'],
    styles: path.resolve(APP_DIR, 'sass/css.js'),
    main: path.resolve(APP_DIR, 'js/index.jsx'),
  },
  output: {
    path: BUILD_DIR,
    filename: '[name].[hash].bundle.js',
  },
  plugins: [
    new ExtractTextPlugin({
      filename: 'styles.[hash].css'
    }),
    new CommonsChunkPlugin({
      names: ['vendor'],
      filename: 'vendor.[hash].js'
    }),
    new BundleTracker({filename: './webpack-stats.json'}),
    new CleanWebpackPlugin([
      BUILD_DIR,
    ], {
      exclude: ['.gitkeep'],
      verbose: true,
      dry: false,
      watch: false,
      allowExternal: false,
    }),
  ],
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        include: APP_DIR,
        loader: 'babel-loader',
        query: {
          presets: ['env', 'stage-2', 'react'],
          plugins: ['transform-object-rest-spread']
        }
      },
      {
        test: /\.scss$/,
        include: APP_DIR,
        loader: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            'css-loader',
            {
              loader: 'postcss-loader',
              options: { plugins: [require('autoprefixer')({ browsers: ['last 2 versions'] })] },
            },
            'sass-loader',
          ]
        })
      },
      {
        test: /\.(png|jpg|gif|ttf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
        loader: "file-loader"
      }
    ]
  }
};

module.exports = config;
