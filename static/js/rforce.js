function UserCtrl($scope, $http) {
    
    $scope.users = [];
    $scope.desc_limit = 50;
        
    $scope.search = function() {
        // console.log('searching..');
        $http.get('/search?q=' + $scope.q).success(function (data) {
            // console.log('got data back');
            $scope.users = data;
        });
    };
}