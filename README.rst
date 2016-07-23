ninja
=====

Simulates N-dice sums (slice and dice, ha). To run the simulations
and process the output::

    $ make install # first time
    $ make

Generates two HTML files complete with tables of values. One contains
the values from simulating rolls (fully deterministic), while the
other contains the one from calculation.

tech details
------------

 - Data from simulations are serialised into JSON-line form using
   `NewlineJSON` Python library.
 - JSON data piped into HTML-generation script using `tablib` to
   generate HTML tables.
 - Uses KaTeX and cheerio from `npm` to pre-render the fractions
   and avoid crashing browser.
 - Makefile to glue all of the components together.
