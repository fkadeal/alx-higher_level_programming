#!/usr/bin/node
const _argv = process.args;
if (_argv === '') {
  console.log('No argument');
} else{
  console.log(_argv);
}
