

document.addEventListener('DOMContentLoaded', function() {


  var calendarEl = document.getElementById('calendar1');


  var calendar1 = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'dayGrid', 'list' ],
    defaultView: 'dayGridMonth',
    header: {
        left: 'prev,next today',
        center:'title',
      // center: 'addEventButton',
      right: 'dayGridMonth,dayGridWeek,listMonth'
    },
      eventLimit: false, 
 
      displayEventTime: false,

      // navLinks: true,
      businessHours:  {
      daysOfWeek: [ 0,1, 2, 3, 4 ],
      },// Monday - Thursday, // display business hours
       eventRender: 

   

      function(info) {

          
       
        var tooltip = new Tooltip(info.el, {
          title: info.event.extendedProps.description,
          placement: 'top',
          trigger: 'hover',
          container: 'body'
        });


       
      },


           eventClick: function(info) {
      
document.write( 
      info.event.title+'<br>'+info.event.extendedProps.description+'<br>'+info.event.end);
  
      },
    
eventOrder:'end',

      events:  [
                {% for l in events %}
                     {
                

                      
                        {% if l.Course_Code == "" %}
                        title: '{{l.title}}',
                        start: '{{ l.start }}',
                        color:'{{ l.color }}',
                        {% endif %}

                        {% if l.Course_Code != "" %}
                        title: '{{l.title}} -> TASK {{l.PART}}',
                        start: '{{ l.start }}',
                        end: '{{ l.end }}',
                        color:'{{ l.color }}',
                        description: '{{ l.Description }}',
                        {% endif %}
                        

                        

                        

                        // url:'/calendar/event'+'{{l.id}}',
                         allDay: false,
  editable: false,
          
                      
                    },

               
                  
                {% endfor %}

               
            ] ,



    
  });


  calendar1.render();
});


