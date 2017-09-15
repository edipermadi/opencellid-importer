## Tables

opencellid-importer creates the following table inside SQLite database
- [cells](#cells-table)
    
### Cells Table

| Column         | Type         | Description                       |
|----------------|--------------|-----------------------------------|
| id *           | INTEGER      | Entry primary key                 |
| radio          | VARCHAR (16) | [Network Type](radio-values.md)   |
| mcc            | INTEGER      | [Mobile Country Code](https://en.wikipedia.org/wiki/Mobile_country_code) |
| net            | INTEGER      | Mobile Network Code (for GSM/UMTS/LTE) or System Identification Number (for CDMA) |
| area           | INTEGER      | Local Area Code (for GSM/UMTS), Tracking Area Code (for LTE) and Network Identification Number (for CDMA) |
| cell           | INTEGER      | Cell Id (for GSM/LTE), UTRAN Cell Id (for UMTS) or Base Station Id (for CDMA) |  
| unit           | INTEGER      |                                   |
| lon            | REAL         | Latitude                          |
| lat            | REAL         | Longitude                         |
| range          | INTEGER      | Estimated range in meters         |
| samples        | INTEGER      | Number of samples assigned to the cell |
| changeable     | INTEGER      | 1 if position is calculated for all measurements |
| created        | INTEGER      | Creation timestamp                |
| updated        | INTEGER      | Last update timestamp             |
| average_signal | INTEGER      | averange signal in dBm            |