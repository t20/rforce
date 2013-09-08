function UserCtrl($scope, $http) {
    
    $scope.users = [];
        
    $scope.search = function() {
        // console.log('searching..');
        $http.get('/search?q=' + $scope.q).success(function (data) {
            // console.log('got data back');
            $scope.users = data;
        });
    };
}