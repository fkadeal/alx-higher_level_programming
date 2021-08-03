#!/usr/bin/node
const _argv = process.argv;
if (_argv[2] === 'undefined') {
  console.log('No argument');
} else{
  console.log(_argv[2]);
}
