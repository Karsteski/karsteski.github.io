Title: CppNorth 2022 Trip Report
Date: 27-07-2022
Modified: 27-07-2022
Category: conferences
Tags: CppNorth, Conference
Slug: CppNorth-2022-Trip-Report

Hello people, I'm Kareem, a junior C++ developer at [Christie Digital](https://www.christiedigital.com/). I'm quite new to software development in general, as I worked at getting better at programming for a number of years whilst working as a chemist. I had signed up to be a volunteer at the CppNorth conference earlier in the year, which I then had to reneg on due to starting my aforementioned job, not wanting to take several days off barely a month in. Luckily and thankfully, my manager was okay with me attending as a volunteer, so I was able to attend my first C++ conference ever!

As a volunteer, our duties were simply to ensure the ancillary parts of the conference ran smoothly, such as the registration table, the timing of the speakers and ensuring the closed captions for each presentation were set up. I arrived in Toronto by train from Stratford, Ontario on the Sunday of the conference, so I unfortunately was unable to attend the weekend workshops. Still, I was happy to be able to help out with the large number of people at the registration table that day.

With respect to the accommodations, the Omni King Edward hotel staff were genuinely friendly and helpful when needed. It was certainly the fanciest hotel I've ever stayed at, not that I have had much experience with that sort of thing. That being said, I was happy that the hotel had a reasonably stocked gym for all guests to use and that there was always (expensive but good) food available.

In terms of the conference itself, the attendees were quite friendly and very open to casual conversation. My fellow volunteers were equally amicable and on the Sunday I got to enjoy some fun games of [Dixit](https://en.wikipedia.org/wiki/Dixit_(card_game)) with them and a few attendees. The board games were for sure a great idea, and I'd definitely like them to make a return.

Now, on to some of the talks I was able to attend at the conference.

---

#### *Opening Keynote: Kate Gregory - "Am I a Good Programmer?"*

In the opening keynote, Kate talks about the metrics people use in determining whether they are good programmers. She noted that measures such as years of employment, age or [large amounts of GitHub contributions]({projects.md}/../../images/articles/cppnorth-2022-trip-report/github-contribution-activity.png) were poor metrics of "a good programmer". I found that one of the strongest points made was that the ceation of long term maintainable code is a strong sign of a good programmer. I will certainly keep this in mind for the decades to come.

Kate Gregory herself is a lady that I've looked up to for years. She has helped me out personally in the [#include <C++> discord](https://www.includecpp.org/discord/) that I have been a part of ever since I began my journey into learning C++ and software development in general. I was quite glad to be able to finally meet someone whose talks and advice I've kept in mind for a quite a while now!

#### *Patrice Roy - Programming for Warm Days: Avoiding Dangerous Conversions*

In this code-heavy session, Patrice demonstrates how one would convert between units of Celsius and Farenheit whilst maintaining type safety and avoiding the use of macros. An important point brought up during this talk was modern C++'s ability to force more compile time errors (i.e. significantly easier to fix). Usage of `<type_traits>` and *user-defined literals* were a highlight, and they will for sure be a part of my C++ toolkit, when appropriate, from here on.

Patrice Roy is someone whom I first learnt about during a C++ Toronto User Group meetup in September 2020. Here, Patrice gave a presentation on "Some things C++ does right". It was quite informative, with that event leading me to emailing Patrice. He gave me some simple but great advice which I followed through on, and for which I am forever thankful. Yet another person in the C++ community I was glad to be able to finally meet.

#### *Jussi Pakkanen - Lessons learned from porting LibreOffice's build system to Meson*

As a user of the Meson build system myself, this was one of the talks I was most interested in attending. Jussi talked about the difficulties in porting the enormous code base of LibreOffice (millions of lines of C++ code) to Meson. One thing I learnt was that if necessary, one can always manually check the verbose output of `$ make` to extract the compiler flags used during a build, to aid in porting to a new build system. Crazy stuff. I hope I never have to do it.

I'm also grateful for Jussi sending me a copy of the Meson Manual last year, when it was no longer available. This solidified my understanding of how Meson works, and is a large reason why I happily use Meson for my personal C++ projects to this day! :)

---

### **Day 2**

#### *Tony Van Eerd - Value Oriented Programming. Part 1: You say you want to write a function*

You want to do something? Call a function. Does the function not exist yet? Write it.
Tony talks a lot about functions, and I understand why. One of the lines he uses in this talk is "Functions are answers to questions". It's a great, short piece of advice that any junior developer such as myself should keep in the back of their mind. This talk was so good I binged a number of Tony's talks this weekend. And you should too.

Here's my main takeaways from this presentation:

- Separate calculation from performing a task with said calculation.
- Returning void is a code smell.
- Naming is hard.
- Minimizing function arguments is a barrier to [complecting](https://www.wordnik.com/words/complect).
- Free functions are cool. Use more of them.

#### *Jason Turner - The Best Parts of C++*

Apparently C++ is a big language. I couldn't tell. Jason distilled many of the newer features of C++ into bite sized topics for everyone (me) to go "Oh right that exists, I should try using it".

Here are some examples of that:

- Variadic templates.
- Fold expressions (C++17).
- Concepts (C++20).
- `std::print` (C++23)
- More `<string_view>`!
- Keep in mind the copy elision compiler optimization!

There's a lot more. Definitely a talk I will rewatch as soon as it's released on the [CppNorth Youtube](https://www.youtube.com/channel/UCGWAlXciy785Iog-X7247Hw).

---

### **Day 3**

#### *Keynote: Tara Walker - "Yes! Robotics for the C++ developer"*

Tara Walker is an amazing speaker. Her excitement for her work in robotics is certainly infectious. In this talk, Tara demonstrates the ease of use of the open source Robot Operating System (ROS). ROS is not so much an OS as a set of frameworks and libraries to build applications that communicate with robots. I had already had the opportunity to listen to Tara talk about just how easy it is for C++ developers to get involved in the robotics community, at yet another C++ Toronto meetup. Her keynote was a good reminder than I need to go back to playing with my Arduino microcontrollers. That's how I got started programming in the first place after all!

#### *Olivier Giroux - Forward Progress in C++*

In this talk, Olivier demonstrates, with some broken examples, the various issues one can encounter whilst doing multithreaded programming. To be honest, a lot of the info during this talk went over my head. It was made clear to me that I need to actually write some multithreaded programs myself to gain a proper understanding of this very important topic in computer science. "Parallel tasks are forbidden from observing each other's effects" is a quote that I will definitely try to keep in mind. Granted, this is a pure definition for a perfect world, but important nonetheless.


On the Monday of the conference, Olivier just happened to sit down with a group of us volunteers at lunch. He mentioned that he now worked for Apple, which led me to asking him about Apple and gaming. From there, he proceeded to spend time doing a very good job of explaining what it means to truly care about the precision and detailed work that makes Apple products great. While I've never been an Apple user myself and for the most part I've completely avoided their products, I was definitely drawn more towards that ecosystem that day. Olivier was genuinely a great person to have been able to have just a casual conversation with. I will do my best to pay attention to the finer details of the software I build. The details of which turn a good product into an amazing one.  

---

### *Summary*

All in all, CppNorth was a fantastic experience. I hope to be able to attend next time it's held, and maybe even give a talk myself some day. It was an event that bolstered my already strong interest in becoming the best programmer that I can, and I hope it has done the same for everyone else! :)






