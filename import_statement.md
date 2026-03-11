Import Statements:

    * import <module>
        - This import statement import all the elements of the module.
        - The elements (functions, classes and variables) can be accessed with this
          syntax: <module>.<element>

    * from <module> import <elem>
        - This import statement only imports the specified element from the module.
        - We can use this element directly, without specifying the name of the module.

    * from <module> import *
        - This is a wildcard import statement. It imports all the elements from the module.
        - We do not need to specify the name of the module to use or call the elements.

    * import <module> as <name>
        - This import statement is used to import a module with a different name, 
          so we can use this new name in our code.
        - The elements can be accessed with <name>.<element>.