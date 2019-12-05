## Regular Expressions ##

Clever 'wild card' expression for matching and parsing strings.

Have to **import re** to use regular expressions in Python.

Can fine-tune what is returned by including regular expressions (e.g. **dot** matches any character, the **asterisk** character is any number of times).

Great to use when workring with uncleant data as can narros down the match signicantly.

re.search() returns a T/F depending on whether the string matches the regular expression.  We use re.findall) if we want the matching strings to be extracted.

The **repeat** characters (* and +) push outward in both directions (greedy) to match the largest possible string.  If you add a **?** the matching becomes non-greedy.