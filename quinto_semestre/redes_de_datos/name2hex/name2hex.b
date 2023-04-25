Get first char
,----------
[
  Fix char
  ++++++++++
  Store 16 to use divmod
  >>++[<++++++++>-]<<
  Perform divmod
  [
    ->-
    [>+>>]
    >[+[-<+>]>+>>]
    <<<<<
  ]
  Reset b minus a mod b (M1)
  >[-]
  Move a / b to M7
  >>[>>>>+<<<<-]
  Move a % b to M8
  <[>>>>>>+<<<<<<-]
  Move to M7 and save TRUE value
  >>>+>>

  Transform char into hex
  [
    Copy to M0 and increase M2
    <<<<<+<<+
    Move to test value
    >>
    Check if it's 10
    [
      Create a copy of M2 in M3
      [>+>+<<-]>>[<<+>>-]<
      Check if the number is 10
      [
        Remove 10
        ----------
        Move to TRUE (M5) or FALSE (M6)
        [>]>>
        Run statements
        [
          Extra for hex number bigger than 9
          <<<<+++++++
          >>>>[-]>
        ]
      ]
    ]
    Reset copy
    <<<[-]>>>
    Go back to the nibble
    >-
  ]
  Reset count and TRUE
  <<[-]<<<[-]
  Turn nibble into a number
  ++++++++[<<++++++>>-]
  Add extra if bigger than 10
  <[<+>-]

  Go to next nibble
  >>>>>+>>

  Transform char into hex
  [
    Copy to M0 and increase M2
    <<<<<+<<+
    Move to test value
    >>
    Check if it's 10
    [
      Create a copy of M2 in M3
      [>+>+<<-]>>[<<+>>-]<
      Check if the number is 10
      [
        Remove 10
        ----------
        Move to TRUE (M5) or FALSE (M6)
        [>]>>
        Run statements
        [
          Extra for hex number bigger than 9
          <<<<+++++++
          >>>>[-]>
        ]
      ]
    ]
    Reset copy
    <<<[-]>>>
    Go back to the nibble
    >-
  ]

  Reset count and TRUE
  <<[-]<<<[-]
  Turn nibble into a number
  ++++++++[<<++++++>>-]
  Add extra if bigger than 10
  <[<+>-]

  Print and go to next nibble
  <<[.>]

  Keep asking until LF
  ,----------
]
Print LF
++++++++++.
