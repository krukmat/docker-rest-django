var angularApp = angular.module('angularApp', ['ngTable', 'ngResource', "infinite-scroll", 'ui.bootstrap.datetimepicker'])

// Class to create the infinite scrolling
angularApp.factory('DataBase', function($resource) {
      var backendAPI = '/event_discovery/';

      var DataBase = function() {
        this.records = [];
        this.busy = false;
        this.page = 1;
        this.filters = {};
        this.error = false;
      };

      DataBase.prototype.reset = function reset() {
        this.page = 1;
        this.records = [];
        this.error = false;
        this.busy = false;
        this.nextPage();
      };

      DataBase.prototype.nextPage = function nextPage() {
        var pointer = this;
        if (this.busy) return;
        if (this.error) return;
        this.busy = true;
        if (this.filters === {}) {
            this.filters = {'page': this.page};
        } else{
            this.filters['page'] = this.page;
        }
        var promise = $resource(backendAPI, this.filters).get().$promise;
        promise.then(function(data) {
              pointer.records = pointer.records.concat(data.results);
              if (data.results.length > 0) {
                pointer.page += 1;
              }
              pointer.busy = false;
              pointer.error = false;
            }, function(){
              pointer.error = true;
              pointer.busy = false;
            });
       };

    return DataBase;
});

angularApp.controller('ContentCtrl',['$resource', '$scope', 'NgTableParams', 'DataBase' , function($resource, $scope, NgTableParams, DataBase){

   $scope.database = new DataBase($resource);

   $scope.dateFilter = new Date();

   function pad(n, len) {

        s = n.toString();
        if (s.length < len) {
            s = ('0000000000' + s).slice(-len);
        }

        return s;

    }

   function convertDateTimeToStr(date){

        var curr_date = date.getDate();
        var curr_month = date.getMonth() + 1; //Months are zero based
        var curr_year = date.getFullYear();
        var curr_hour = date.getHours();
        // Minutes defined in 00.
        return String(curr_year+'-'+pad(curr_month, 2)+'-'+pad(curr_date, 2)+' '+pad(curr_hour, 2)+':00')
   }

   function convertDateToStr(date){

        var curr_date = date.getDate();
        var curr_month = date.getMonth() + 1; //Months are zero based
        var curr_year = date.getFullYear();
        // Minutes defined in 00.
        return String(curr_year+'-'+pad(curr_month, 2)+'-'+pad(curr_date, 2))
   }



    // datetime picker
    $scope.onTimeSet = function onTimeSet(field, fromDate){
        var toDate = angular.copy(fromDate);
        // TODO: Remove this. First It need improve backend filters
        // TODO: remove $scope.dateFilter from model. Use an auxiliary variable
        toDate.setTime(toDate.getTime() + (60*60*1000)); // Increase 1 hour
        $scope.database.filters[field + '_from'] = convertDateTimeToStr(fromDate);
        $scope.database.filters[field + '_to'] = convertDateTimeToStr(toDate);
        $scope.database.reset();

    }

    $scope.onDateSet = function onDateSet(field, fromDate){
        $scope.database.filters[field] = convertDateToStr(fromDate);
        $scope.database.reset();
    }

    $scope.onTextSet = function onTextSet(field, value) {
        $scope.database.filters[field+'_start'] = value;
        $scope.database.reset();
    }

}]);