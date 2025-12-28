const arr = [
    {
        url: "https://www.armandoalpantheon.it/wp-content/uploads/2023/03/Primavera-a-Roma-%E2%80%93-Il-Colosseo-e-gli-scavi-di-Ostia-Antica-armando-al-pantheon-768x480.jpg",
        title: "Colosseo",
        description: "Originariamente conosciuto come Anfiteatro Flavio è il più grande anfiteatro romano del mondo.",
    },
    {
        url: "https://www.donne.it/wp-content/uploads/2023/10/intelligenza-artificiale-768x512.jpg",
        title: "Intelligenza Artificiale",
        description: "Nel suo significato più ampio, è la capacità di un sistema artificiale di simulare l'intelligenza umana attraverso l'ottimizzazione di funzioni matematiche.",
    },
    /*{
        url: "https://png.pngtree.com/background/20230525/original/pngtree-floral-wallpaper-with-brown-and-brown-paint-picture-image_2735082.jpg",
        title: "Linguaggio dei fiori",
        description: "Modo di comunicazione ottocentesco per cui i fiori e gli allestimenti floreali venivano utilizzati per esprimere sensazioni che non sempre potevano essere pronunciate.",
    }*/
];


function createCard(data) {
    // div representing a card
    var card = document.createElement("div");
    card.className = "bg-white rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-shadow";

    // Create the image element
    
    // Append the image to Card div

    // Div for the title and the paragraph (textcontainer)
    
    // Create the title element
    
    // Append the title to the textcontainer div

    // Create the description element
    
    // Append the paragraph to the textcontainer div

    // Append the textcontainer to the Card div
   
    // Append the created card to the container
    document.getElementById("container").appendChild(card);
    
}
