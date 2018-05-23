# Changelog

## 1.4.0 - 1.4.1 (2018-05-22)

- Include currency in account structure

**required changes**

- File format version changed from `v1` to `v2`, adapt etl
 

## 1.3.0 - 1.3.1 (2018-03-06) 

- Retry for a given amount of times the download of any account in case of XML parsing errors
- Tolerate ParseError to apply retry logic, as well



## 1.2.0 - 1.2.2 (2017-09-21)
 
- Make the config and click commands discoverable in [mara-app](https://github.com/mara/mara-app) >= 1.2.0
- Fix problem for relative path
- Import pycriteo package only when needed (importing results in https requests for a wsdl file being made)


## 1.1.0 - 1.1.1 (2017-05-17)

- fixed dictionary structure which allowed only for one campaign per day
- Ad explicit dependency for suds


## 1.0.0 - 1.0.2 (2017-03-02) 

- Initial version
- made cli and config discoverable
- removed click default values to make compatable with mara
