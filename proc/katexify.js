#!/usr/bin/env node

const getStdin = require('get-stdin');
const cheerio  = require('cheerio');
const katex    = require('katex');

getStdin().then(str => {
  const $ = cheerio.load(str, {
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
