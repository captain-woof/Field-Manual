---
title: Strings
created: '2020-10-01T05:03:18.795Z'
modified: '2020-10-01T05:10:56.650Z'
---

# Strings

### Declaration:

var s = new String();

### Methods:

- **String.prototype.charAt(index)**
    Returns the character (exactly one UTF-16 code unit) at the specified index.
- **String.prototype.charCodeAt(index)**
    Returns a number that is the UTF-16 code unit value at the given index.
- **String.prototype.codePointAt(pos)**
    Returns a nonnegative integer Number that is the code point value of the UTF-16 encoded code point starting at the specified pos.
- **String.prototype.concat(str [, ...strN ])**
    Combines the text of two (or more) strings and returns a new string.
- **String.prototype.includes(searchString [, position])**
    Determines whether the calling string contains searchString.
- **String.prototype.endsWith(searchString [, length])**
    Determines whether a string ends with the characters of the string searchString.
- **String.prototype.indexOf(searchValue [, fromIndex])**
    Returns the index within the calling String object of the first occurrence of searchValue, or -1 if not found.
- **String.prototype.lastIndexOf(searchValue [, fromIndex])**
    Returns the index within the calling String object of the last occurrence of searchValue, or -1 if not found.
- **String.prototype.localeCompare(compareString [, locales [, options]])**
    Returns a number indicating whether the reference string compareString comes before, after, or is equivalent to the given string in sort order.
- **String.prototype.match(regexp)**
    Used to match regular expression regexp against a string.
- **String.prototype.matchAll(regexp)**
    Returns an iterator of all regexp's matches.
- **String.prototype.normalize([form])**
    Returns the Unicode Normalization Form of the calling string value.
- **String.prototype.padEnd(targetLength [, padString])**
    Pads the current string from the end with a given string and returns a new string of the length targetLength.
- **String.prototype.padStart(targetLength [, padString])**
    Pads the current string from the start with a given string and returns a new string of the length targetLength.
- **String.prototype.repeat(count)**
    Returns a string consisting of the elements of the object repeated count times.
- **String.prototype.replace(searchFor, replaceWith)**
    Used to replace occurrences of searchFor using replaceWith. searchFor may be a string or Regular Expression, and replaceWith may be a string or function.
- **String.prototype.replaceAll(searchFor, replaceWith)**
    Used to replace all occurrences of searchFor using replaceWith. searchFor may be a string or Regular Expression, and replaceWith may be a string or function.
- **String.prototype.search(regexp)**
    Search for a match between a regular expression regexp and the calling string.
- **String.prototype.slice(beginIndex[, endIndex])**
    Extracts a section of a string and returns a new string.
- **String.prototype.split([sep [, limit] ])**
    Returns an array of strings populated by splitting the calling string at occurences of the substring sep.
- **String.prototype.startsWith(searchString [, length])**
    Determines whether the calling string begins with the characters of string searchString.
- **String.prototype.substr()**
    Returns the characters in a string beginning at the specified location through the specified number of characters.
- **String.prototype.substring(indexStart [, indexEnd])**
    Returns a new string containing characters of the calling string from (or between) the specified index (or indeces).
- **String.prototype.toLocaleLowerCase( [locale, ...locales])**

    The characters within a string are converted to lowercase while respecting the current locale.

    For most languages, this will return the same as toLowerCase().
- **String.prototype.toLocaleUpperCase( [locale, ...locales])**

    The characters within a string are converted to uppercase while respecting the current locale.

    For most languages, this will return the same as toUpperCase().
- **String.prototype.toLowerCase()**
    Returns the calling string value converted to lowercase.
- **String.prototype.toString()**
    Returns a string representing the specified object. Overrides the Object.prototype.toString() method.
- **String.prototype.toUpperCase()**
    Returns the calling string value converted to uppercase.
- **String.prototype.trim()**
    Trims whitespace from the beginning and end of the string. Part of the ECMAScript 5 standard.
- **String.prototype.trimStart()**
    Trims whitespace from the beginning of the string.
- **String.prototype.trimEnd()**
    Trims whitespace from the end of the string.
- **String.prototype.valueOf()**
    Returns the primitive value of the specified object. Overrides the Object.prototype.valueOf() method.
- **String.prototype.@@iterator()**
    Returns a new Iterator object that iterates over the code points of a String value, returning each code point as a String value. 

### HTML Wrapper Methods

- **String.prototype.anchor()**
    `<a name="name"> (hypertext target)`
- **String.prototype.big()**
    `<big>`
- **String.prototype.blink()**
    `<blink>`
- **String.prototype.bold()**
    `<b>`
- **String.prototype.fixed()**
    `<tt>`
- **String.prototype.fontcolor()**
    `<font color="color">`
- **String.prototype.fontsize()**
   `<font size="size">`
- **String.prototype.italics()**
    `<i>`
- **String.prototype.link()**
    `<a href="url"> (link to URL)`
- **String.prototype.small()**
    `<small>`
- **String.prototype.strike()**
    `<strike>`
- **String.prototype.sub()**
    `<sub>`
- **String.prototype.sup()**
    `<sup> `
