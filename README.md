# Library for Automation testing on Digital Instrument cluster HMI
This repository contains the APIs required for Automation testing on Digital instrument clusters.
<table>
  <thead>
    <tr>
      <th>Method Name</th>
      <th>Description</th>
      <th>Return Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>initialise_webdriver</td>
      <td>Initiaises the webdriver. Uses Mozilla Firefox browser with geckodriver support</td>
      <td>Returns the driver object</td>
    </tr>
    <tr>
      <td>get_url</td>
      <td>Launches the cluster HMI display over the browser</td>
      <td>None</td>
    </tr>
    <tr>
      <td>press_btn</td>
      <td>Presses the button in the Cluster HMI</td>
      <td>None</td>
    </tr>
    <tr>
      <td>setup_logger</td>
      <td>Starts the logging service</td>
      <td>Logger object and Log path</td>
    </tr>
    <tr>
      <td>capture_screen</td>
      <td>Captures the screenshot at an instance</td>
      <td>Returns the path of the saved screenshot image</td>
    </tr>
    <tr>
      <td>icon_db_load</td>
      <td>Loads the icon.sql which contains all the images into icons.db database</td>
      <td>None</td>
    </tr>
    <tr>
      <td>read_database_icon_and_save</td>
      <td>checks for the given icon name in the icon database and converts it to image and stores in the logs</td>
      <td>None</td>
    </tr>
    <tr>
      <td>verify_telltale_status</td>
      <td>This method Checks the presence of the telltale icon in the HMI</td>
      <td>True/False</td>
    </tr>
    <tr>
      <td>verify_warning_status</td>
      <td>This method will check the given warning text is present in the HMI</td>
      <td>True/False</td>
    </tr>
    <tr>
      <td>enable_logger</td>
      <td>Logging functionality is enabled here.</td>
      <td>Logger object and Log path</td>
    </tr>
    <tr>
      <td>get_connection</td>
      <td>Creates the database icons.db and makes a connection with it</td>
      <td>connection and cursor object</td>
    </tr>
    <tr>
      <td>create_table</td>
      <td>Creates the table for storing the images with their names</td>
      <td>None</td>
    </tr>
    <tr>
      <td>execute_sql_file</td>
      <td>Executes the icons.sql file which inserts all the images into the icons.db</td>
      <td>None</td>
    </tr>
    <tr>
      <td>insert_image</td>
      <td>Method to convert image to hex code for storing into the database</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
