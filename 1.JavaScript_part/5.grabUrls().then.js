grabUrls().then( function( urls ) {
    urls = urls.join( '\n' );
    createDownload( urls );
} );