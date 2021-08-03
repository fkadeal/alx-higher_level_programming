#!/usr/bin/node
const _argv = process.argv;
if (_argv[3] === '') {
  console.log('No argument');
} else{
  console.log(_argv[3]);
}
