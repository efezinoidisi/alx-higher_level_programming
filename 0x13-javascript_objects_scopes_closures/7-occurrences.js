#!/usr/bin/node

// This function returns the number of occurrences of a number in a list

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      num++;
    }
  }
  return (num);
};
