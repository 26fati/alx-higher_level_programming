#!/usr/bin/node
exports.esrever = function (list) {
  const lst = [];
  for (let i = 0; i < list.length; i++) {
    lst.unshift(list[i]);
  }
  return (lst);
};
