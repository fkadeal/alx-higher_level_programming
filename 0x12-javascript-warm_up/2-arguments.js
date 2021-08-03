#!/usr/bin/node
  var _argv = process.argv.length;
console.log(_argv);
if(_argv === 3){
console.log('Argument found');
}else if(_argv == 2){
  console.log('No argument');
}else if(_argv > 3){
  console.log('Argument found');
}
