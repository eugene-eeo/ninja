#!/usr/bin/env node

var getStdin = require('get-stdin');
var cheerio  = require('cheerio');
var katex    = require('katex');

getStdin().then(function(str) {
  var $ = cheerio.load(str, {
    normalizeWhitespace: true
  });
  $('tr td:last-child').each(function() {
    var td = $(this);
    var text = td.text();
    var html = katex.renderToString(text);
    td.html(html);
  });
  console.log($.html());
});
