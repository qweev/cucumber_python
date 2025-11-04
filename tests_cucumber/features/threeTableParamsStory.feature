Feature: three table params story

  Scenario Outline: three scenario with table
    Given three variable <aParam>
    When three I add with <bParam>
    Then three system output is <valueParam>
    Examples:
      | aParam | bParam | valueParam |
      | 2      | 3      | 5          |
      | 4      | 3      | 7          |
      | 6      | 3      | 9          |