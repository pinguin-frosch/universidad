Get first char
,----------
[
  Fix char
  ++++++++++

  Perform divmod
  >>++[<++++++++>-]<<
  [
    ->-
    [>+>>]
    >[+[-<+>]>+>>]
    <<<<<
  ]

  Ignore second value
  >[-]

  Move nibbles
  >>[>>>>+<<<<-]
  <[>>>>>>+<<<<<<-]
  >>>+>>

  [
    Move to correct location
    <<<<<+<<+

    Check if it's 10
    >>
    [
      Create a copy
      [>+>+<<-]>>[<<+>>-]<

      [
        ----------

        Perform IF
        [>]>>
        [
          Extra for hex number bigger than 9
          <<<<+++++++>>>>[-]>
        ]
      ]
    ]

    Reset copy and go back
    <<<[-]>>>>-
  ]

  Reset count and TRUE
  <<[-]<<<[-]

  Turn into hex representation
  ++++++++[<<++++++>>-]<[<+>-]

  Go to next nibble
  >>>>>+>>

  [
    Copy to correct location
    <<<<<+<<+

    Check if it's 10
    >>
    [
      Create a copy
      [>+>+<<-]>>[<<+>>-]<

      [
        ----------

        Perform IF
        [>]>>
        [
          Extra for hex number bigger than 9
          <<<<+++++++
          >>>>[-]>
        ]
      ]
    ]

    Reset copy and go back
    <<<[-]>>>>-
  ]

  Reset count and TRUE
  <<[-]<<<[-]

  Turn into hex representation
  ++++++++[<<++++++>>-]<[<+>-]

  Print hex representation
  <<[.>]

  Keep recording chars
  ,----------
]

Print LF
++++++++++.
