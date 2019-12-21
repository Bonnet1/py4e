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

**Javascript Object Notation**
* may never need to use XML as it can be too powerful for what we need
* serialization format that is being used most
* data returns as a dictionary
* can also return as a list (containing dictionaries)

**Service Oriented Approach / Architecture**
* best example is an airline booking website -- reads data to allow car/hotel booking too
* build using **application process interface** (API)
* e-framework provides the standard to create a service oriented architecture (dead project)

**Using Application Programming Interfaces (API)**
* more common to be the consumer than producer of API
* e.g. google maps API geocodes addresses
* may have security and rate limiting (generally charge for access)
* authentication and authorization normally used