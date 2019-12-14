## Web Services ##

Two commonly used format for exchanging data (**Wire Protocol**)
* XML
* JSON

e.g. XML:
<person>
    <name>Chuck</name>
    <phone type="intl">303-4456</number>
</person>

**eXtensible Markup Language (XML)**
* became popular around the same tine as HTML and has simple elements/nodes like HTML
* primary purpose is to **share structured data**
* has start tag, end tag, text content, attribute, and self closing tag
* serialize/de-serialize related to tasks when transferring across network
* think of XML as a tree, child and parent nodes
* can also think of as a path -- walk down the paths to get the result

**XML Schema**
* desribes a contract that is acceptible for XML between systems
* modern schema is from W3C (XSD) -- otherwise schema's are available but rarely used
* can add constraints to set min and max number of variables, and set data types to share info
