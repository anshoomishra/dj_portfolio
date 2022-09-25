var slideUp = {
    distance: '20%',
    origin: 'left',
    opacity: 1,
    delay: 300
};

var slideLeft = {
    distance: '20%',
    origin: 'left',
    opacity: 1,
    delay: 1000
};
var slideRight = {
    distance: '20%',
    origin: 'right',
    opacity: 1,
    delay: 1000
};
ScrollReveal().reveal('.reveal-skillProgramingLanguage',slideUp);
ScrollReveal().reveal('.reveal-skillDatabase', slideUp);
ScrollReveal().reveal('.reveal-skillBackEndTechnologies',slideUp);

ScrollReveal().reveal('.reveal-skillFrontEndTechnologies',slideUp);


//ScrollReveal().reveal('.company-joining-date',slideLeft);
//ScrollReveal().reveal('.company-joining-status',slideRight);