# cluster_hmi_test_lib
This repository contains the APIs required for Automation testing on Digital instrument clusters.

<table>
  <tr>
    <th>Method name</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>initialise_webdriver</td>
    <td>Selenium webdriver is initialised</td>
    <td>get_url</td>
    <td>Launches the Cluster HMI over the firefox browser</td>
    <td>press_btn</td>
    <td>Function to click on the buttons in the HMI</td>
    <td>setup_logger</td>
    <td>Provides the logging service</td>
    <td>capture_screen</td>
    <td>Captures the screenshot for validation</td>
    <td>icon_db_load</td>
    <td>Loads all the icons present in icon.sql to icon database</td>
    <td> verify_telltale_statu</td>
    <td>Tnis method takes 3 parameters(telltale_mode, icon_data, frame_data). This API validates the status of the given icon in the HMI (ON/OFF)</td>
    <td>verify_warning_status</td>
    <td>This method takes 3 parameters(warning_status, warning_id, frame_data). This API validates the status of the given warning ID in the HMI (ON/OFF)</td>
  </tr>
</table>
