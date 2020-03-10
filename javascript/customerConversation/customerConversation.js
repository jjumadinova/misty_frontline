/* Runs script to talk with customer. */

SetVolumeForSkill();
misty.Pause(3000);
WelcomePhase();
misty.Pause(43000);

StorytellingPhase();
misty.Pause(20000);

SurprisePhase();
misty.Pause(10000);

FarewellPhase();
misty.Pause(10000);

misty.DisplayImage("e_DefaultContent.jpg");


function SetVolumeForSkill() {
    misty.SetDefaultVolume(5);
}

function WelcomePhase() {
    var welcome1 = '<speak>Hi, welcome to Fedawn 1919 </speak>';
    var welcome2 = '<speak> My name is Misty and I\'m your robot sales assistant for today.</speak>';
    var welcome3 = '<speak> I hope your experience with Fedawn 1919 can bring you joy!</speak>';
    var welcome4 = '<speak>\
                    I\'m happy to present you with the Fedawn 1919 exclusive store! \
                    Inside you can find key holders, wallets, passport holders, pouches and bags. \
                    You can also find school supplies like agenda, pencil holders and backpacks. \
                    As you can see, our main colors are black, orange and blue. \
                    All products are branded Fedawn 1919 and are Italian leather. \
                    Additionally today everything is special discounted up to sixty percent off! \
                    You can find prices near or inside the merchandise. \
                    You may buy up to two items of your liking \
                    </speak>';
    misty.Speak(welcome1);
    misty.Pause(1000);
    misty.DisplayImage("e_Admiration.jpg");
    misty.Pause(3000);
    misty.Speak(welcome2);
    misty.DisplayImage("e_DefaultContent.jpg");
    misty.Pause(3000);
    misty.Speak(welcome3);
    misty.DisplayImage("e_Surprise.jpg");
    misty.Pause(3000);
    misty.DisplayImage("e_DefaultContent.jpg");
    misty.Pause(3000);
    misty.Speak(welcome4);
    misty.DisplayImage("e_Love.jpg");
    misty.Pause(3000);
}

function StorytellingPhase() {
    var story1 = '<speak> I would like to share with you a magical story of Fedawn 1919.</speak>';
    var story2 = '<speak> \
                In Rome the famous actress Sophia Loren was waiting alone for an airplane. \
                She was going to a set to take part in a movie and she was carrying a lot of bags. \
                Mr. Giorgio Fedawn loved cinema and he recognized her immediately. \
                He kindly asked her with her heavy luggage and they spent the next hour talking about cinema. \
                </speak>';
    var story3 = '<speak> \
                When Giorgio Fedawn came back home, he started working on a new model of bag inspired by his time with Sofia Lauren. \
                That was the first bag in Fedawn\'s history: a large, soft and light bag with leather handles, ideal for a train journey. \
                You can find two behind me! \
                </speak>';
    misty.Speak(story1);
    misty.DisplayImage("e_Joy.jpg");
    misty.Pause(5000);
    misty.Speak(story2);
    misty.DisplayImage("e_DefaultContent.jpg");
    misty.Pause(22000);
    misty.Speak(story3);
    misty.DisplayImage("e_Love.jpg");
    misty.Pause(3000);
}

function SurprisePhase() {
    var surprise1 = '<speak> \
                    Thank you for visiting our Fedawn 1919 exclusive store \
                    We really appreciate your time! To show you our thanks, we would like to give you a special gift. \
                    </speak>'
    var surprise2 = '<speak> \
                    The gift is in the bin on the wall. Feel free to take the present. I hope you like it! \
                    </speak>';
    misty.Speak(surprise1);
    misty.DisplayImage("e_Joy.jpg");
    misty.Pause(13000);
    misty.DisplayImage("e_DefaultContent.jpg");
    misty.Speak(surprise2);
    misty.DisplayImage("celebration.jpg");
    misty.Pause(7000);
    misty.DisplayImage("e_DefaultContent.jpg");
}

function FarewellPhase() {
    var farewell = '<speak> It was nice to meet you. I wish you a wonderful day </speak>';
    misty.Speak(farewell);
    misty.DisplayImage("e_Joy.jpg");
    misty.Pause(5000);
    misty.DisplayImage("e_Sleepy.jpg");
    misty.Pause(1000);
    misty.DisplayImage("e_Sleepy2.jpg");
    misty.Pause(1000);
    misty.DisplayImage("e_Sleepy3.jpg");
    misty.Pause(1000);
    misty.DisplayImage("e_Sleepy4.jpg");
    misty.Pause(1000);
    misty.DisplayImage("e_SleepingZZZ.jpg");
}